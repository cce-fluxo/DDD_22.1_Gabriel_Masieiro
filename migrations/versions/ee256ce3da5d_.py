"""empty message

Revision ID: ee256ce3da5d
Revises: 6b8f713d0ce0
Create Date: 2022-09-23 17:48:50.371226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee256ce3da5d'
down_revision = '6b8f713d0ce0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('authorship',
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], )
    )
    op.create_table('file_tag',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.drop_table('arquivo')
    op.add_column('file', sa.Column('creationTimeStamp', sa.DateTime(), nullable=True))
    op.add_column('file', sa.Column('type', sa.String(length=100), nullable=True))
    op.add_column('file', sa.Column('click_quantity', sa.Integer(), nullable=True))
    op.add_column('file', sa.Column('category', sa.String(length=100), nullable=True))
    op.add_column('file', sa.Column('year', sa.Integer(), nullable=True))
    op.add_column('file', sa.Column('awarded', sa.String(length=100), nullable=True))
    op.add_column('file', sa.Column('description', sa.String(length=100), nullable=True))
    op.add_column('file', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.alter_column('file', 'area',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.create_foreign_key(None, 'file', 'user', ['creator_id'], ['id'])
    op.drop_column('file', 'ano')
    op.drop_column('file', 'upload')
    op.drop_column('file', 'descricao')
    op.drop_column('file', 'categoria')
    op.drop_column('file', 'autores')
    op.drop_column('file', 'titulo')
    op.drop_column('file', 'tags')
    op.drop_column('file', 'premiacao')
    op.add_column('user', sa.Column('verificationPinHash', sa.LargeBinary(length=128), nullable=True))
    op.add_column('user', sa.Column('createdPinTimestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'createdPinTimestamp')
    op.drop_column('user', 'verificationPinHash')
    op.add_column('file', sa.Column('premiacao', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('tags', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('titulo', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('autores', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('categoria', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('descricao', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('upload', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('file', sa.Column('ano', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'file', type_='foreignkey')
    op.alter_column('file', 'area',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.drop_column('file', 'creator_id')
    op.drop_column('file', 'description')
    op.drop_column('file', 'awarded')
    op.drop_column('file', 'year')
    op.drop_column('file', 'category')
    op.drop_column('file', 'click_quantity')
    op.drop_column('file', 'type')
    op.drop_column('file', 'creationTimeStamp')
    op.create_table('arquivo',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('titulo', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('descricao', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('upload', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('categoria', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('area', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('ano', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('autores', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('tags', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('premiacao', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='arquivo_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='arquivo_pkey')
    )
    op.drop_table('file_tag')
    op.drop_table('authorship')
    op.drop_table('tag')
    op.drop_table('author')
    # ### end Alembic commands ###
