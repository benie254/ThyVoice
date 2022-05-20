"""a migration.

Revision ID: 9b506a8ed8cf
Revises: 
Create Date: 2022-05-17 01:03:41.382780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b506a8ed8cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_id')
    # ### end Alembic commands ###