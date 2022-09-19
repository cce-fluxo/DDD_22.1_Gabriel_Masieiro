"""empty message

Revision ID: 6b8f713d0ce0
Revises: 836702d7fd6e
Create Date: 2022-09-19 10:34:16.821162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b8f713d0ce0'
down_revision = '836702d7fd6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('arquivo', sa.Column('titulo', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('descricao', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('upload', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('categoria', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('area', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('ano', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('autores', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('tags', sa.String(length=80), nullable=False))
    op.add_column('arquivo', sa.Column('premiacao', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('arquivo', 'premiacao')
    op.drop_column('arquivo', 'tags')
    op.drop_column('arquivo', 'autores')
    op.drop_column('arquivo', 'ano')
    op.drop_column('arquivo', 'area')
    op.drop_column('arquivo', 'categoria')
    op.drop_column('arquivo', 'upload')
    op.drop_column('arquivo', 'descricao')
    op.drop_column('arquivo', 'titulo')
    # ### end Alembic commands ###
