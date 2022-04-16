from invoke import task


@task
def wait_for(ctx, host, timeout=30):
    ctx.run(f"wait-for-it {host} --timeout={timeout}")


@task
def makemigrations(ctx):
    ctx.run("python manage.py makemigrations")


@task
def migrate(ctx, noinput=False):
    options = []
    if noinput:
        options.append("--noinput")

    options = " ".join(options)
    ctx.run(f"python manage.py migrate {options}")


@task
def runserver(ctx, host="0.0.0.0", port=8000):
    command = f"python manage.py runserver {host}:{port}"
    ctx.run(command, pty=True)


@task
def test(ctx, args=""):
    """This task executes pytest command with the given arguments but before the execution it waits
    the needed services

    Args:
        ctx: context
        args (str, optional): arguments for pytest splitted by spaces. Defaults to "".
    """
    wait_for(ctx, "testredis:6379")
    wait_for(ctx, "testdb:3306")
    wait_for(ctx, "testelasticsearch:9200")

    command = "py.test"

    args = [command, args]
    ctx.run(" ".join(args), pty=True)
