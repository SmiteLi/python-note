#!/usr/bin/env bash
git add base/*
git add spider/*
git commit -m "update repo at `date +'%Y-%m-%d %H:%M:%S'`"
git push
