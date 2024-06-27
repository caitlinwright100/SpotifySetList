# Introduction
This repository contains the code which built the website: [spotifysetlistcreator.com](https://spotifysetlistcreator.com). The website purpose is to automate the process of creating a spotify playlist in a spotify account, which reflects an artist's most recent setlist from [Setlist FM](www.setlistfm.com).

# Instructions
1) Follow the link to the website and input an artist name
2) Click "create playlist"
3) Enter Spotify login details
4) Follow link to new Spotify playlist

# How it Works
1) Once artist name is inputted, Fast API is used to connect to the Setlist FM API and searches for the most recent setlist of that artist
2) The artist name and setlist are stored as cookies in the browser, whilst Fast API connects to the Spotify Web Development API so that the user can input their login details
3) Once the user has logged in to their Spotify account, the cookies are retrieved and the playlist is created using the Spotipy python package
4) The website is running on an AWS instance that automatically reboots when changes are made to the code, via Github actions
5) The code is packaged as a Docker container which builds an image on AWS ECR each time a change is made


# Tools, Skills, and Notable Packages Used
- Python
- Pytest
- Spotipy
- Fast API
- Docker
- Github Actions
- AWS - EC2, ECR, IAM, Route 53
- Bash
- HTML
- VS Code

# Upcoming Updates
- Create a release.yaml github action to automate refreshing the instance
- Create different versions of the environment, dev, preprod, and prod
- Run unit tests and integration tests as part of github action
- Use react to create a more versatile frontend for the website, including a loading spinner
- Use terraform so that cloud infrastructure can be versioned and reused
  
