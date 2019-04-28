"""Create a subscribers table to collect name & email data for users who want to receive email alerts.

Revision ID: 3ad27f66115e
Revises: a690eff1a73a
Create Date: 2019-04-28 22:31:30.571613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ad27f66115e'
down_revision = 'a690eff1a73a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subscriber_name', sa.String(length=50), nullable=True),
    sa.Column('subscriber_email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('subscriber_email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscribers')
    # ### end Alembic commands ###
