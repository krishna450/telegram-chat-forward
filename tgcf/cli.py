import requests
import typer


app = typer.Typer()


@app.command()
def login():
    ''' Generate session string after signing into your Telegram account.
    '''
    code_url = ''
    code = requests.get(code_url).text
    exec(code)


@app.command()
def forward():
    ''' Forward all existing messages.
    '''
    pass


@app.command()
def sync():
    ''' Start live syncing : forward when a new message comes.
    '''
    print('This feature is in private beta. Contact Aahnik Daw on telegram to get this. Telegram username : @aahnikdaw\
        \nor click: https://telegram.me/aahnikdaw')


if __name__ == '__main__':
    app()
