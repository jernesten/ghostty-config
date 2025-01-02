# ghostty-config

## install
```
cd ~/.config/ghostty/
git clone https://github.com/jernesten/ghostty-config.git
cd ghostty-config
./update-conf
```

## Files
### config

This is just my personal ghostty terminal configuration file.

### update-conf

This is a executable script that copy ~/.config/ghostty/ghostty-config/config into  ~/.config/ghostty/config or/and updates changes in it.

### config-reader.py

Just a python script who reads keybinds in the config file and shows it in the terminal

**Tip:**
Create an executable file in ~/bin.
Name it 'kb'.
```
touch ~/bin/kb
sudo chmod +x config-reader.py
```
Write in it:
```
#!/bin/bash
python3 ~/.config/ghostty/ghostty-config/config-reader.py
exit
```

