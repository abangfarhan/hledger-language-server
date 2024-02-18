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

@server.feature(TEXT_DOCUMENT_COMPLETION)
def completions(params: CompletionParams):
    """Returns completion items."""
    output = (subprocess
              .check_output(['hledger', 'accounts'])
              .decode()
              .strip())
    lst = output.split('\r\n')
    items = [CompletionItem(label=x) for x in lst]
    return CompletionList(
        is_incomplete=False,
        items=items,
    )

def main():
    server.start_io()
