"""add url to video

Revision ID: c8de9a496ae9
Revises: 78002f2f7d18
Create Date: 2023-03-24 17:34:12.318229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8de9a496ae9'
down_revision = '78002f2f7d18'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('videos', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('videos', 'url')
    # ### end Alembic commands ###