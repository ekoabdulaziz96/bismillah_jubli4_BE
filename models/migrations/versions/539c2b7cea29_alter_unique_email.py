"""alter unique email

Revision ID: 539c2b7cea29
Revises: 6eb6b01abbb2
Create Date: 2022-04-01 10:53:07.300025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '539c2b7cea29'
down_revision = '6eb6b01abbb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user_recipients', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_recipients', type_='unique')
    # ### end Alembic commands ###
