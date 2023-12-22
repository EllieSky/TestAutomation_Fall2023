from behave import step

from tests import ADMIN_USER, PASSWORD


@step('I am loggen in as ADMIN')
@step('I am loggen in as user "{username}" with password "{password}"')
def login(context, username=ADMIN_USER, password=PASSWORD):
    context.page.login.authenticate(username, password)


@step('the welcome message should be "{message}"')
def check_welcome_message(context, message):
    assert message == context.menu.user.get_welcome_message()


@step('I logout')
def logout(context):
    context.menu.user.logout()