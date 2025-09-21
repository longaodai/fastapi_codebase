"""create coupons table

Revision ID: 2d0feeb8e9a7
Revises: 
Create Date: 2025-09-21 12:26:43.780461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d0feeb8e9a7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'coupons',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('code', sa.String(length=255), unique=True, index=True, nullable=False),
        sa.Column('type', sa.SmallInteger, nullable=False),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('expiry_date', sa.DateTime, nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),  # default = now()
        ),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),  # default = now()
            onupdate=sa.func.now(),        # auto update timestamp
        ),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4'
    )

    op.execute("""
        INSERT INTO coupons (code, type, value, expiry_date)
        VALUES
            ('SALE10', 1, 10, NOW() + INTERVAL 7 DAY),
            ('DISCOUNT50K', 2, 50000, NOW() + INTERVAL 30 DAY),
            ('OLD20', 1, 20, NOW() - INTERVAL 1 DAY),
            ('FOREVER100', 2, 100000, NULL),
            ('SOFTDELETE', 1, 15, NOW() + INTERVAL 10 DAY)
    """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('coupons')
    pass
