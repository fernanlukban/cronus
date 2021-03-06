"""Added event table

Revision ID: 30573f3f422d
Revises: 032e1263522b
Create Date: 2018-12-30 21:30:36.213652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30573f3f422d'
down_revision = '032e1263522b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('event')
    # ### end Alembic commands ###
