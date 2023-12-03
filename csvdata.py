import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def getMatchesPerYear(mathcesrows):
    allYears = []
    years = []
    matchPerYear = []
    s1 = slice(0, 4)

    for row in mathcesrows:
        allYears.append(row[2][s1])
        if row[2][s1] not in years:
            years.append(row[2][s1])

    for year in years:
        matchPerYear.append(allYears.count(year))

    # for year, matchCnt in zip(years, matchPerYear):
    #     print(f"year: {year}, mathces: {matchCnt}")

    fig, ax = plt.subplots()
    ax.set_title("Mathces Per Year")
    ax.set_xlabel("year")
    ax.set_ylabel("number of mathces")
    ax.bar(years, matchPerYear)
    plt.show()


def getMathcesWonByPerTeam(mathcesrows):
    teams = [
        "RCB",
        "KKR",
        "CSK",
        "DC",
        "RR",
        "PKings",
        "SRH",
        "MI",
        "Kochi",
        "RPS",
        "GL",
    ]

    mathces_won = [0] * 11

    for row in mathcesrows:
        match row[10]:
            case "Royal Challengers Bangalore":
                mathces_won[0] += 1
            case "Kolkata Knight Riders":
                mathces_won[1] += 1
            case "Chennai Super Kings":
                mathces_won[2] += 1
            case "Delhi Capitals":
                mathces_won[3] += 1
            case "Delhi Daredevils":
                mathces_won[3] += 1
            case "Rajasthan Royals":
                mathces_won[4] += 1
            case "Punjab Kings":
                mathces_won[5] += 1
            case "Kings XI Punjab":
                mathces_won[5] += 1
            case "Deccan Chargers":
                mathces_won[6] += 1
            case "Sunrisers Hyderabad":
                mathces_won[6] += 1
            case "Mumbai Indians":
                mathces_won[7] += 1
            case "Kochi Tuskers Kerala":
                mathces_won[8] += 1
            case "Rising Pune Supergiants":
                mathces_won[9] += 1
            case "Rising Pune Supergiant":
                mathces_won[9] += 1
            case "Gujarat Lions":
                mathces_won[10] += 1

    # for team, wonCnt in zip(teams, mathces_won):
    #     print(f"team: {team}, mathces won: {wonCnt}")

    fig, ax2 = plt.subplots()
    ax2.set_title("Mathces Won By Per Team")
    ax2.set_xlabel("Teams")
    ax2.set_ylabel("Number Of Matches")
    ax2.bar(teams, mathces_won)
    plt.show()


def getMatchesPerCity(mathcesrows):
    totalMathces = []
    venue = []
    venueCnt = []
    for row in mathcesrows:
        totalMathces.append(row[1])
        if row[1] not in venue:
            venue.append(row[1])
    for ven in venue:
        venueCnt.append(totalMathces.count(ven))

    # for ven, vnct in zip(venue, venueCnt):
    #     print(f"venue: {ven}, mathces played: {vnct}")

    fig, ax4 = plt.subplots()
    ax4.set_title("Number Of Mathces Per City")
    ax4.set_xlabel("City")
    ax4.set_xticks(range(len(venue)), venue, rotation="vertical")
    ax4.set_ylabel("Number Of Mathces")
    ax4.bar(venue, venueCnt)
    plt.show()


def getExtraRunsPerTeamIn2016(ballsrows):
    # year 2016 starting id = 980901
    # year 2016 ending id = 981017

    ballsData2016 = []
    for ball in ballsrows:
        if int(ball[0]) >= 980901 and int(ball[0]) <= 981017:
            ballsData2016.append(ball)

        teams = [
            "RCB",
            "KKR",
            "DC",
            "PKings",
            "SRH",
            "MI",
            "RPS",
            "GL",
        ]

    extraRuns = [0] * 8

    for ball in ballsData2016:
        match ball[-1]:
            case "Royal Challengers Bangalore":
                extraRuns[0] += int(ball[8])
            case "Kolkata Knight Riders":
                extraRuns[1] += int(ball[8])
            case "Delhi Daredevils":
                extraRuns[2] += int(ball[8])
            case "Kings XI Punjab":
                extraRuns[3] += int(ball[8])
            case "Sunrisers Hyderabad":
                extraRuns[4] += int(ball[8])
            case "Mumbai Indians":
                extraRuns[5] += int(ball[8])
            case "Rising Pune Supergiants":
                extraRuns[6] += int(ball[8])
            case "Gujarat Lions":
                extraRuns[7] += int(ball[8])

    # for run, team in zip(extraRuns, teams):
    #     print(f"team: {team}, run:{run}")

    fig, ax3 = plt.subplots()
    ax3.set_title("Extra Runs Conceded Per Team In The Year 2016")
    ax3.set_xlabel("Teams")
    ax3.set_ylabel("Extra Runs")
    ax3.bar(teams, extraRuns)
    plt.show()


# working with mathc file data
matchesfile = "csv\ipl_matches.csv"
mathcesrows = []
with open(matchesfile, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        mathcesrows.append(row)
getMatchesPerYear(mathcesrows)
getMathcesWonByPerTeam(mathcesrows)
getMatchesPerCity(mathcesrows)


# working with balls file data
ballsfile = "csv\ipl_balls.csv"
ballsrows = []
with open(ballsfile, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        ballsrows.append(row)
getExtraRunsPerTeamIn2016(ballsrows)
