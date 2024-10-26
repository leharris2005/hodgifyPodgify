public class sampleCode {
    // For all requests an access token is needed
    SpotifyApi spotifyApi = new SpotifyApi.Builder()
            .setAccessToken("taHZ2SdB-bPA3FsK3D7ZN5npZS47cMy-IEySVEGttOhXmqaVAIo0ESvTCLjLBifhHOHOIuhFUKPW1WMDP7w6dj3MAZdWT8CLI2MkZaXbYLTeoDvXesf2eeiLYPBGdx8tIwQJKgV8XdnzH_DONk")
            .build();

    // Create a request object with the optional parameter "market"
    final GetSomethingRequest getSomethingRequest = spotifyApi.getSomething("qKRpDADUKrFeKhFHDMdfcu")
            .market(CountryCode.SE)
            .build();

    void getSomething_Sync() {
        try {
            // Execute the request synchronous
            final Something something = getSomethingRequest.execute();

            // Print something's name
            System.out.println("Name: " + something.getName());
        } catch (Exception e) {
            System.out.println("Something went wrong!\n" + e.getMessage());
        }
    }

    void getSomething_Async() {
        try {
            // Execute the request asynchronous
            final Future<Something> somethingFuture = getSomethingRequest.executeAsync();

            // Do other things...

            // Wait for the request to complete
            final Something something = somethingFuture.get();

            // Print something's name
            System.out.println("Name: " + something.getName());
        } catch (Exception e) {
            System.out.println("Something went wrong!\n" + e.getMessage());
        }
    }