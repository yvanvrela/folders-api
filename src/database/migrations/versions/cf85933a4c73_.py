"""empty message

Revision ID: cf85933a4c73
Revises: 
Create Date: 2022-08-14 23:36:29.264050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf85933a4c73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contribuyentes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('ruc', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ruc')
    )
    op.create_table('folders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contribuyente_id', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('time', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['contribuyente_id'], ['contribuyentes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('folders')
    op.drop_table('contribuyentes')
    # ### end Alembic commands ###
