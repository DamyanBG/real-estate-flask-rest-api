"""Add land

Revision ID: 95979d057d0a
Revises: ed8c6f0d7b6b
Create Date: 2023-07-13 15:49:14.939055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95979d057d0a'
down_revision = 'ed8c6f0d7b6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    with op.batch_alter_table('visitations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('land_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'lands', ['land_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visitations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('land_id')

    op.drop_table('lands')
    # ### end Alembic commands ###