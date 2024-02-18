hledger-language-server is a simple hledger language server. I've only
tested this on Neovim with the CoC plugin. This project depends on the
pygls library (https://github.com/openlawlibrary/pygls).

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

Future improvements:

- [ ] Use user configurations to determine hledger executable
- [ ] Use user configurations to determine hledger file to parse
- [ ] Use caching to improve performance
