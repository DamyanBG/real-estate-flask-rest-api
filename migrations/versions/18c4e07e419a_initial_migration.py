"""Initial migration

Revision ID: 18c4e07e419a
Revises: 
Create Date: 2024-03-30 12:06:14.423474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18c4e07e419a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('user', 'seller', 'admin', name='roletype'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('homes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('neighborhood', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=255), nullable=False),
    sa.Column('size', sa.String(length=255), nullable=False),
    sa.Column('year', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('longitude', sa.String(length=255), nullable=True),
    sa.Column('latitude', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('photo_url', sa.String(length=255), nullable=True),
    sa.Column('home_views', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('place', sa.String(length=255), nullable=False),
    sa.Column('price', sa.String(length=255), nullable=False),
    sa.Column('size', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('longitude', sa.String(length=255), nullable=True),
    sa.Column('latitude', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('photo_url', sa.String(length=255), nullable=True),
    sa.Column('land_views', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.Column('invitor_id', sa.Integer(), nullable=True),
    sa.Column('invited_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'accepted', 'rejected', name='meetingstatustype'), nullable=False),
    sa.Column('home_id', sa.Integer(), nullable=True),
    sa.Column('land_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_id'], ['homes.id'], ),
    sa.ForeignKeyConstraint(['invited_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['invitor_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['land_id'], ['lands.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visitations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('start_hour', sa.Time(), nullable=False),
    sa.Column('end_hour', sa.Time(), nullable=False),
    sa.Column('organizator_id', sa.Integer(), nullable=True),
    sa.Column('home_id', sa.Integer(), nullable=True),
    sa.Column('land_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['home_id'], ['homes.id'], ),
    sa.ForeignKeyConstraint(['land_id'], ['lands.id'], ),
    sa.ForeignKeyConstraint(['organizator_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visitations')
    op.drop_table('meetings')
    op.drop_table('lands')
    op.drop_table('homes')
    op.drop_table('users')
    # ### end Alembic commands ###
