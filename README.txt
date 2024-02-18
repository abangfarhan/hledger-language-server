hledger-language-server is a simple hledger language server. I've only
tested this on Neovim with the CoC plugin.

Installation:

>> pip install .

Put the following in coc-settings.json file (run :CocConfig from inside
Neovim):

{
  # ... other configs
  "languageserver": {
    "hledger": {
      "command": "hledger-language-server",
      "filetypes": ["ledger"]
    }
  }
}
