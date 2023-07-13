"""Add Home

Revision ID: 218ca12130c1
Revises: 
Create Date: 2023-07-13 12:25:40.233887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218ca12130c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('neighborhood', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=255), nullable=False),
    sa.Column('size', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('longitude', sa.String(length=255), nullable=True),
    sa.Column('latitude', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('photo_url', sa.String(length=255), nullable=True),
    sa.Column('home_views', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homes')
    # ### end Alembic commands ###