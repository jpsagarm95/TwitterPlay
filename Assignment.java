import twitter4j.FilterQuery;
import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;

public class Assignment {

      private static String consumerKey = "65arhtNIobmbjy5gVm9Hjp4Kw";
	  private static String consumerSecret = "YcGF1YGw1gtAWWz1vSwJN5LZRB7P02xqULzd7TtB5E6ITLYzH8";
	  private static String accessToken = "3279486750-BVQWfGE7QwMRs3tnnHYCipsQGW4dQIRwjV5ChEx";
	  private static String accessTokenSecret = "5PezaKGEoTv4YJSt6CrVghkl62xF76Cifx81EIYZtPDXo";
	  private static twitter4j.TwitterStream twitterStream;
	  
	  public static void main(String args[]){
	  	  FilterQuery tweetFilterQuery = new FilterQuery();
	  	  String a[] = {"en"};
	  	  tweetFilterQuery.language(a);
	  	  
	  	ConfigurationBuilder _configurationBuilder = new ConfigurationBuilder();
		    _configurationBuilder.setOAuthConsumerKey(consumerKey)
		    					 .setOAuthConsumerSecret(consumerSecret)
		    					 .setOAuthAccessToken(accessToken)
		    					 .setOAuthAccessTokenSecret(accessTokenSecret)
		    					 .setJSONStoreEnabled(true);
		    
		    twitterStream = new TwitterStreamFactory(_configurationBuilder.build()).getInstance();
		    StatusListener listener = new StatusListener() {
				
				@Override
				public void onException(Exception arg0) {
					System.out.println("Error occured: "+ arg0.getMessage());
					arg0.printStackTrace();
				}
				
				@Override
				public void onTrackLimitationNotice(int arg0) {
	                System.out.println("Track limitation notice for " + arg0);								
				}
				
				@Override
				public void onStatus(Status status) {
					if(status.getLang().equals("en"))
						System.out.println(status.getText().replaceAll("[\n\r]", ""));
				}
				
				@Override
				public void onStallWarning(StallWarning arg0) {
					// TODO Auto-generated method stub
					
				}
				
				@Override
				public void onScrubGeo(long arg0, long arg1) {
					// TODO Auto-generated method stub
					
				}
				
				@Override
				public void onDeletionNotice(StatusDeletionNotice arg0) {
					// TODO Auto-generated method stub
					
				}
			};    	
			twitterStream.addListener(listener);	  	  
	
			twitterStream.sample();  
	}

	
	
}

