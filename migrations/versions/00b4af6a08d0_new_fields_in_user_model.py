"""new fields in user model

Revision ID: 00b4af6a08d0
Revises: e04e3d554f7a
Create Date: 2021-02-25 21:16:00.379502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00b4af6a08d0'
down_revision = 'e04e3d554f7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###