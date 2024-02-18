from pygls.server import LanguageServer
from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    CompletionItem,
    CompletionList,
    CompletionOptions,
    CompletionParams,
)
import subprocess

server = LanguageServer('hledger-language-server', 'v0.1')
items_cache = []

@server.feature(TEXT_DOCUMENT_COMPLETION)
def completions(params: CompletionParams):
    """Returns completion items."""
    global items_cache

    try:
        output = (subprocess
                  .check_output(['hledger', 'accounts'])
                  .decode()
                  .strip())
        lst = output.splitlines()
        items = [CompletionItem(label=x) for x in lst]
        items_cache = items
    except subprocess.CalledProcessError:
        items = items_cache

    return CompletionList(
        is_incomplete=False,
        items=items,
    )

def main():
    server.start_io()
