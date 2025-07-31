from api.src.model.account import Account
from api.src.repository.account_repo import save, delete

def save_and_delete_account():
    account = Account('-1', 'goodboy', 'good@boy.human', '123456789', None)

    assert save(account)
    assert delete(account.id)
    assert save(account)

if __name__ == '__main__':
    save_and_delete_account()