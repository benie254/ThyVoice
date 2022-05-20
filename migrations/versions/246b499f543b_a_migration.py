"""a migration.

Revision ID: 246b499f543b
Revises: 9b506a8ed8cf
Create Date: 2022-05-17 01:08:06.435636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246b499f543b'
down_revision = '9b506a8ed8cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'blog_pic_path')
    # ### end Alembic commands ###