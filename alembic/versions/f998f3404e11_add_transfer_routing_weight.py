"""add_transfer_routing_weight

Revision ID: f998f3404e11
Revises: 9a2b4ec0fd71
Create Date: 2021-05-24 00:59:25.248767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f998f3404e11'
down_revision = '9a2b4ec0fd71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transfer_routing', sa.Column('weight', sa.Integer(), nullable=True))
    op.execute('Update transfer_routing set weight = 0 where weight is null')
    op.alter_column('transfer_routing', 'weight', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transfer_routing', 'weight')
    # ### end Alembic commands ###