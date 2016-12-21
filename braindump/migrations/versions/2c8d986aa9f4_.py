"""empty message

Revision ID: 2c8d986aa9f4
Revises:
Create Date: 2016-12-20 14:57:13.963577

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '2c8d986aa9f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tag', sa.String(length=200), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=True),
                    sa.Column('updated_date', sa.DateTime(), nullable=True),
                    sa.Column('email', sa.String(length=254), nullable=True),
                    sa.Column('password_hash', sa.String(
                        length=256), nullable=True),
                    sa.Column('confirmed', sa.Boolean(), nullable=True),
                    sa.Column('avatar_hash', sa.String(
                        length=32), nullable=True),
                    sa.Column('last_login_date', sa.DateTime(), nullable=True),
                    sa.Column('default_notebook', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_created_date'), 'users',
                    ['created_date'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_updated_date'), 'users',
                    ['updated_date'], unique=False)
    op.create_table('notebooks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=True),
                    sa.Column('updated_date', sa.DateTime(), nullable=True),
                    sa.Column('title', sa.String(length=200), nullable=True),
                    sa.Column('is_deleted', sa.Boolean(), nullable=True),
                    sa.Column('author_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_notebooks_created_date'),
                    'notebooks', ['created_date'], unique=False)
    op.create_index(op.f('ix_notebooks_updated_date'),
                    'notebooks', ['updated_date'], unique=False)
    op.create_table('notes',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=True),
                    sa.Column('updated_date', sa.DateTime(), nullable=True),
                    sa.Column('title', sa.String(length=200), nullable=True),
                    sa.Column('body', sa.Text(), nullable=True),
                    sa.Column('author_id', sa.Integer(), nullable=True),
                    sa.Column('notebook_id', sa.Integer(), nullable=True),
                    sa.Column('is_deleted', sa.Boolean(), nullable=True),
                    sa.Column('is_favorite', sa.Boolean(), nullable=True),
                    sa.Column('is_archived', sa.Boolean(), nullable=True),
                    sa.Column('search_vector',
                              sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(
                        ['notebook_id'], ['notebooks.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_notes_created_date'), 'notes',
                    ['created_date'], unique=False)
    op.create_index(op.f('ix_notes_updated_date'), 'notes',
                    ['updated_date'], unique=False)
    op.create_table('note_tag',
                    sa.Column('note_id', sa.Integer(), nullable=True),
                    sa.Column('tag_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['note_id'], ['notes.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(
                        ['tag_id'], ['tags.id'], ondelete='CASCADE')
                    )
    op.create_table('shared_notes',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=True),
                    sa.Column('updated_date', sa.DateTime(), nullable=True),
                    sa.Column('author_id', sa.Integer(), nullable=True),
                    sa.Column('note_id', sa.Integer(), nullable=True),
                    sa.Column('recipient_email', sa.String(
                        length=254), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['note_id'], ['notes.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_shared_notes_created_date'),
                    'shared_notes', ['created_date'], unique=False)
    op.create_index(op.f('ix_shared_notes_updated_date'),
                    'shared_notes', ['updated_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shared_notes_updated_date'),
                  table_name='shared_notes')
    op.drop_index(op.f('ix_shared_notes_created_date'),
                  table_name='shared_notes')
    op.drop_table('shared_notes')
    op.drop_table('note_tag')
    op.drop_index(op.f('ix_notes_updated_date'), table_name='notes')
    op.drop_index(op.f('ix_notes_created_date'), table_name='notes')
    op.drop_table('notes')
    op.drop_index(op.f('ix_notebooks_updated_date'), table_name='notebooks')
    op.drop_index(op.f('ix_notebooks_created_date'), table_name='notebooks')
    op.drop_table('notebooks')
    op.drop_index(op.f('ix_users_updated_date'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_created_date'), table_name='users')
    op.drop_table('users')
    op.drop_table('tags')
    # ### end Alembic commands ###
