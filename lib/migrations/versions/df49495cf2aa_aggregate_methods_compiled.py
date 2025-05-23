"""aggregate methods compiled

Revision ID: df49495cf2aa
Revises: a252e31288a4
Create Date: 2025-05-23 15:02:45.029533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df49495cf2aa'
down_revision = 'a252e31288a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('freebies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('dev_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('fk_freebies_company_id_companies')),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name=op.f('fk_freebies_dev_id_devs')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('freebie')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('freebie',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_name', sa.VARCHAR(), nullable=True),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.Column('company_id', sa.INTEGER(), nullable=True),
    sa.Column('dev_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='fk_freebie_company_id_companies'),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name='fk_freebie_dev_id_devs'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('freebies')
    # ### end Alembic commands ###
