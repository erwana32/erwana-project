# finance_core/management/commands/seed_coa.py
from django.core.management.base import BaseCommand
from finance_core.models import Account

class Command(BaseCommand):
    help = 'Seed Chart of Accounts (COA) dasar untuk sistem Finance & Accounting'

    def handle(self, *args, **options):
        coa_list = [
            ('1101', 'Kas', 'ASSET'),
            ('1102', 'Bank', 'ASSET'),
            ('1103', 'Piutang Usaha', 'ASSET'),
            ('1201', 'Persediaan Barang Dagang', 'ASSET'),
            ('1301', 'Peralatan', 'ASSET'),
            ('1401', 'Akumulasi Penyusutan', 'ASSET'),
            ('2101', 'Hutang Usaha', 'LIABILITY'),
            ('2102', 'Hutang Gaji', 'LIABILITY'),
            ('2103', 'Pajak Terutang', 'LIABILITY'),
            ('3101', 'Modal Pemilik', 'EQUITY'),
            ('3102', 'Laba Ditahan', 'EQUITY'),
            ('4101', 'Penjualan Barang', 'INCOME'),
            ('4102', 'Retur Penjualan', 'INCOME'),
            ('5101', 'Harga Pokok Penjualan (HPP)', 'EXPENSE'),
            ('6101', 'Beban Gaji', 'EXPENSE'),
            ('6102', 'Beban Listrik', 'EXPENSE'),
            ('6103', 'Beban Sewa', 'EXPENSE'),
            ('6104', 'Beban Operasional Lainnya', 'EXPENSE'),
        ]

        for code, name, acc_type in coa_list:
            account, created = Account.objects.get_or_create(
                code=code,
                defaults={
                    'name': name,
                    'account_type': acc_type,
                    'is_group': False,
                    'is_active': True,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Akun {code} - {name} ditambahkan."))
            else:
                self.stdout.write(self.style.WARNING(f"Akun {code} - {name} sudah ada, dilewati."))

        self.stdout.write(self.style.SUCCESS('✅ Chart of Accounts (COA) dasar berhasil dimasukkan.'))
