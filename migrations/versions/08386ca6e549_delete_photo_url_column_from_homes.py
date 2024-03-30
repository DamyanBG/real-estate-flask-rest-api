"""Delete photo_url column from homes

Revision ID: 08386ca6e549
Revises: ea81f760c7e1
Create Date: 2024-03-30 23:43:06.166154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08386ca6e549'
down_revision = 'ea81f760c7e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('homes', schema=None) as batch_op:
        batch_op.drop_column('photo_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('homes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo_url', sa.VARCHAR(length=255), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
