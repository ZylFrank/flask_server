from . import main
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    return User.query().all()
