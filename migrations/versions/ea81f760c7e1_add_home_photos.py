"""Add home photos

Revision ID: ea81f760c7e1
Revises: 2f3f8ed17896
Create Date: 2024-03-30 23:04:33.170983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea81f760c7e1'
down_revision = '2f3f8ed17896'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('home_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo_url', sa.String(length=255), nullable=True),
    sa.Column('home_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_id'], ['homes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('home_photos')
    # ### end Alembic commands ###