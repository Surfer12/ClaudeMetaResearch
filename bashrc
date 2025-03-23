BASHRC=$( [ -f "$HOME/.bash_profile" ] && echo "$HOME/.bash_profile" || echo "$HOME/.bashrc" )
echo 'eval "$(magic completion --shell bash)"' >> "$BASHRC"
export PATH="$PATH:'/home/ryanoatespro/.modular/bin/'"
source "$BASHRC"
