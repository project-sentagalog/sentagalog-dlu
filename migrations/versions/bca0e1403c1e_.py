"""empty message

Revision ID: bca0e1403c1e
Revises: 
Create Date: 2019-10-03 02:15:49.084966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bca0e1403c1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('label_history',
    sa.Column('label_id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('tweet_id', sa.Integer(), nullable=True),
    sa.Column('sentiment', sa.Integer(), nullable=True),
    sa.Column('reason_for_sentiment', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('label_id')
    )
    op.create_index(op.f('ix_label_history_label_id'), 'label_history', ['label_id'], unique=False)
    op.create_table('tweets',
    sa.Column('instance_id', sa.Integer(), nullable=False),
    sa.Column('tweet_id', sa.String(length=128), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('text', sa.String(length=460), nullable=True),
    sa.Column('created_at', sa.String(length=256), nullable=True),
    sa.Column('language', sa.String(length=15), nullable=True),
    sa.Column('search_term', sa.String(length=64), nullable=True),
    sa.Column('dataset_domain', sa.String(length=64), nullable=True),
    sa.Column('sentiment', sa.Integer(), nullable=True),
    sa.Column('labeller', sa.Integer(), nullable=True),
    sa.Column('reason_for_sentiment', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('instance_id')
    )
    op.create_index(op.f('ix_tweets_instance_id'), 'tweets', ['instance_id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('first_name', sa.String(length=120), nullable=True),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_users_password'), 'users', ['password'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_password'), table_name='users')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tweets_instance_id'), table_name='tweets')
    op.drop_table('tweets')
    op.drop_index(op.f('ix_label_history_label_id'), table_name='label_history')
    op.drop_table('label_history')
    # ### end Alembic commands ###
