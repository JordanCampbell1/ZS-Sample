"""add cascade delete for blogs when  user deletion occurs

Revision ID: 7347905b4bc9
Revises: 6c86e8d772c7
Create Date: 2025-07-07 14:32:02.712995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7347905b4bc9'
down_revision: Union[str, Sequence[str], None] = '6c86e8d772c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
