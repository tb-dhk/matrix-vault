---
title: how does matrix ACTUALLY work though
date: 2008-01-15
tags:
  - matrix
  - dev-diary
number: 0
hide: true
description: a sequel to the matrix dev diary
---
i'm beginning to realise, after drafting out the first we are 1 dev diary, that my original matrix dev diary was very overly short. it was more of a faq page than a dev diary to be completely honest. there's no actual documentation of how it works other than the platforms i used. so i thought i'd just talk about it here for anyone who's interested.

there's not gonna be a lot of jargon here because i get that not everyone is into this stuff and i find it really hard to keep up with jargon as well so i totally get it. i'll define terms for the sake of anyone who wants to look this stuff up but otherwise i'm mostly going to be using more basic and generic wording.
# backend
the backend is basically an obsidian vault. for those of you who are unaware, obsidian is a note-taking app that organises everything into vaults. each vault is like a directory of markdown files, which are basically files that you can write text in, but you can also add things to them to make them look fancy. most texting apps have their own flavor of markdown (e.g. putting asterisks or underscores around words to make them bold or italic).

each file has six properties.