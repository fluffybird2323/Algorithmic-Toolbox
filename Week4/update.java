public static void updatelocationIdToSiteMap(String newLocId, SystemInfo systemInfo){

        if(LocationIdToSiteMap.locationIdToSiteMap.containsKey(newLocId)) {

            LocationIdToSiteMap.locationIdToSiteMap.get(newLocId).add(systemInfo.getId());
        }
        else{

            LocationIdToSiteMap.locationIdToSiteMap.put(newLocId, new ArrayList<>(Arrays.asList(systemInfo.getId())));
        }
    }
