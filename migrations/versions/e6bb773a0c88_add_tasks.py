"""Add Tasks

Revision ID: e6bb773a0c88
Revises: c052ae5abc1d
Create Date: 2016-12-02 13:52:02.519370

"""

# revision identifiers, used by Alembic.
revision = 'e6bb773a0c88'
down_revision = 'c052ae5abc1d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('note_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('priority', sa.Enum('p0', 'p1', 'p2', name='taskpriority'), nullable=True),
    sa.Column('status', sa.Enum('s0', 's1', 's2', 's3', 's4', name='taskstatus'), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['note_id'], ['notes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_created_date'), 'tasks', ['created_date'], unique=False)
    op.create_index(op.f('ix_tasks_due_date'), 'tasks', ['due_date'], unique=False)
    op.create_index(op.f('ix_tasks_updated_date'), 'tasks', ['updated_date'], unique=False)
    op.drop_constraint('notebooks_author_id_fkey', 'notebooks', type_='foreignkey')
    op.create_foreign_key(None, 'notebooks', 'users', ['author_id'], ['id'])
    op.drop_constraint('notes_author_id_fkey', 'notes', type_='foreignkey')
    op.create_foreign_key(None, 'notes', 'users', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.create_foreign_key('notes_author_id_fkey', 'notes', 'users', ['author_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'notebooks', type_='foreignkey')
    op.create_foreign_key('notebooks_author_id_fkey', 'notebooks', 'users', ['author_id'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_tasks_updated_date'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_due_date'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_created_date'), table_name='tasks')
    op.drop_table('tasks')
    # ### end Alembic commands ###