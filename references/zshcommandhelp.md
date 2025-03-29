add gh to ~/.zshrc

To add GitHub (gh) to your .zshrc file, you can use the following steps:

1. Open the .zshrc file in a text editor:
```javascript
nano ~/.zshrc
```
2. Add the following line to the file, saving it:
```css
alias gh="git -c core.askpass=true -c credential.helper='!gh auth git-credential'"
```
This line sets up a GitHub alias that uses the GitHub CLI to authenticate and interact with GitHub repositories.

3. Save the file and exit the text editor.
4. Reload the .zshrc file:
```bash
source ~/.zshrc
```
5. Verify that the alias has been added:
```bash
type gh
```
You should see the output:
```bash
gh is an alias for git -c core.askpass=true -c credential.helper='!gh auth git-credential'