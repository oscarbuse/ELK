#!/usr/bin/bash
if [ "$1" == "test" ]; then
  scp search_stories.py www.kwalinux.nl:/var/tmp
else
  scp search_stories.py www.kwalinux.nl:
fi
