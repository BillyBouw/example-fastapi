"""add content column to post table

Revision ID: f98d6a4461d7
Revises: 55d60dbbcfb0
Create Date: 2023-03-01 16:42:05.955565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f98d6a4461d7'
down_revision = '55d60dbbcfb0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
