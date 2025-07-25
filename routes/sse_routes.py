# main.py
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from auth import get_current_user
from database import get_db
from redis_utils import subscribe
import asyncio
from sqlalchemy.orm import Session


router = APIRouter(prefix="/sse")


# might need heartbeat if proxies are killing idle connections
@router.get("/events")
async def sse_endpoint(request: Request, db: Session = Depends(get_db)):

    # authentication check

    token = request.query_params.get("token")

    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    user = get_current_user(token=token, db=db)

    # for channel in ["updates", "notifications"]:
    channel = request.query_params.get(
        "channel", "create_blog"  # default channel
    )  # defaults on updates - for blog creation

    async def event_stream():
        pubsub = await subscribe(channel)
        try:
            while True:
                message = await pubsub.get_message(
                    ignore_subscribe_messages=True, timeout=1.0
                )
                if message:
                    yield f"data: {message['data']}\n\n"
                # await asyncio.sleep(0.01)
                if await request.is_disconnected():
                    break
        finally:
            await pubsub.unsubscribe("updates")
            await pubsub.close()

    return StreamingResponse(event_stream(), media_type="text/event-stream")
