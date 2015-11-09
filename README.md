# tri-sync
A encapsulation of rsync command for routine backup.

# Installtion:

1. Run `git clone https://github.com/d0u9/tri-sync`.
2. Create a config file - `.private.json` - in your home directory, and add
it the following content:

```
{
  "Applications": {
    "rsync": {
      "profile1": {
        "server": "XXX.XXX.XXX.XXX",
        "name": "Your username",
        "local": "The fold you want to sync",
        "rmote": "The remote sync path on the remote host"
		}
      "profile2": {
        "server": "XXX.XXX.XXX.XXX",
        "name": "Your username",
        "local": "The fold you want to sync",
        "rmote": "The remote sync path on the remote host"
      }
    }
  }
}
```

3. Replace the `server`, `name`, `local`, `rmote` fields as yours.

# Usage:

Sync local to remote using profile1:

```
tri-sync profile1
```

Sync local to remote using profile1, and delete extraneous files from dest dirs:

```
tri-sync profile1 out -d
```

Sync remote to local:

```
tri-sync profile1 in
```

Sync remote to local and delete extraneous files from dest dirs:

```
tri-sync profile1 in -d
```

# License
![CC License](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)
