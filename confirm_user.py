# To confirm user by email address
# To run: pipenv run invenio shell confirm_user.py <email>

from flask_security.confirmable import confirm_user
from invenio_accounts.proxies import current_datastore
from invenio_db import db
from invenio_users_resources.services.users.tasks import reindex_user
import sys

email=sys.argv[1]
user = current_datastore.get_user(email)
confirm_user(user)
db.session.commit()
reindex_user(user.id)
