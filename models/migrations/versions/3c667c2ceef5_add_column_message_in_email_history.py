"""add column message in email history

Revision ID: 3c667c2ceef5
Revises: 2fa9991194d9
Create Date: 2022-04-03 01:44:08.142997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c667c2ceef5'
down_revision = '2fa9991194d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_histories', sa.Column('message', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('email_histories', 'message')
    # ### end Alembic commands ###
