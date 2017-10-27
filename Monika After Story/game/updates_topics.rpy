# Module that defines changed topics between versions
# this should run before updates.rpy

# start by initalization version update dict
define updates.version_updates = {}

# key:version number -> v:changedIDs
# changedIDs structure:
#   k:oldId -> v:newId
define updates.topics = {}

# runs before updates.rpy
init 9 python:

    if persistent.version_number != config.version:

        # versions
        vv033 = "v033"
        vv032 = "v032"
        vv031 = "v031"
        vv030 = "v030"
        vv022 = "v022"

        # test version
        vv050 = "v050"
        vv100 = "v100"


        # update this dict accordingly to every new version
        # k:old version number -> v:new version number
#        updates.version_updates[vv050] = vv100
#        updates.version_updates[vv033] = vv050
        updates.version_updates[vv032] = vv033
        updates.version_updates[vv031] = vv032
        updates.version_updates[vv030] = vv031
        updates.version_updates[vv022] = vv030


        # version structures:
        # TEST version 0.3.3 -> 1.0.0
        changedIDs = dict()
        changedIDs["monika_test1"] = "monika_test5"
        changedIDs["monika_test3"] = None
        changedIDs["monika_test2"] = "monika_test6"
        changedIDs["monika_test4"] = None
        newIDs = list()
        newIDs.append("this is new")
        newIDs.append("so is this")
        newIDs.append("this is also new")
        updates.topics[vv100] = changedIDs

        # TEST VERSION 2 (0.3.3 -> 0.5.0)
        updates.topics[vv050] = None

        # 0.3.2 -> 0.3.3
        newIDs = ["monika_ribbon"]
        updates.topics[vv033] = None

        # 0.3.1 -> 0.3.2
        changedIDs = dict()
        changedIDs["monika_monika"] = None
        newIDs = [
            "monika_images",
            "monika_herself",
            "monika_prisoner",
            "monika_vnanalysis",
            "monika_ravel",
            "monika_torment",
            "monika_recursion",
            "monika_lain",
            "monika_szs",
            "monika_kyon"
        ]
        updates.topics[vv032] = changedIDs

        # 0.3.0 -> 0.3.1
        changedIDs = dict()
        changedIDs["monika_ghosts"] = "monika_whispers"
        newIDs = [
            "monika_monika",
            "monika_birthday",
            "monika_eyecontact",
            "monika_othergames",
            "monika_playerswriting",
            "monika_ghost"
        ]
        updates.topics[vv031] = changedIDs

        # 0.2.2 -> 0.3.0
        # TODO


