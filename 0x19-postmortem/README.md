<h1>0x19-postmortem</h1>
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--L4jgoCKg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2AnkWf1zVrZ3DCZgnsZAXLWg.jpeg"></img>
<h2>Issue Summary</h2>
<p>On December 1st, 5:45pm to 5:15pm. There a page server error was reported. Users were unable to access page contents after reloading. This affected all users and prevented them from accessing valuable data. </p>
<ul>
Timeline
<li>issue was discovered at 5:45pm</li>
<li>A Beta user picked up the error when he tried reloading the page</li>
<li>I Desire Barine, was alerted immediately. I assumed it was a server related issue. However, on closer inspection i noticed the issue stemed from the fetch function in the frontend. </li>
<li>Valuable time was wasted on debugging the error on the server side</li>
<li>Fortunately the issue did not need escalation</li>
<li>The issue was resolved by implementing caching to display data when reloaded</li>
</ul>
<ul>
Root cause and resolution:
<li>As stated above the error was caused due to the fetch function not activating on reload. This resulted in a blank page. </li>
<li>Caching of data was used to retain user data. This enabled the user data to be available for use on repopulating the page.</li>
</ul>
<ul>
Corrective and preventative measures:
<li>Corrective measures included thorough testing to ensure resolution methods worked</li>
<li>This error is less likely to occur in future.</li>
</ul>
