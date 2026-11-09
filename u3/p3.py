# Unit 3 practice items P33-P35, added in review pass 3 (Nov 8, 2026) for coverage gaps the ChatGPT Pro review
# named: dialects (no direct item), scale analysis (thin), gender and use of space (one item).
P = []

P.append(dict(id="U3-P33", topic="3.7", lo="IMP-3.B", skill="1.D", difficulty="easy",
  stem="English speakers in the southern United States, New England, and the Upper Midwest can understand one another, but they differ in pronunciation and in some everyday words. For example, a soft drink is often called \"soda\" in New England, \"pop\" in much of the Midwest, and \"coke\" in much of the South. These regional varieties of English are best described as",
  options={
    "A": "separate language families",
    "B": "pidgins",
    "C": "dialects",
    "D": "lingua francas",
    "E": "language isolates"},
  answer="C",
  explanation="A dialect is a regional or social version of one language. Speakers of different dialects can usually understand each other, but they use different sounds, words, or grammar. \"Soda,\" \"pop,\" and \"coke\" are a classic example in American English. A line on a map that marks where one word or sound stops and another starts is called an isogloss.",
  whyNot={
    "A": "A language family is a group of related languages. These are all varieties of one language, English.",
    "B": "A pidgin is a contact language for people who share no language. These speakers all speak English.",
    "D": "A lingua franca is a shared language used by people with different first languages. Here everyone already shares English.",
    "E": "A language isolate has no known relatives, like Basque. English belongs to the Indo-European family."},
  vocab=["dialect", "isogloss", "language family"]))

P.append(dict(id="U3-P34", topic="3.3", lo="PSO-3.D", skill="5.D", difficulty="hard",
  stimulus=dict(type="table",
    title="LANGUAGE SPOKEN AT HOME, BY REGION, COUNTRY H (HYPOTHETICAL DATA)",
    columns=["Region", "Share of Country H's population (%)", "Speak Language A at home (%)", "Speak Language B at home (%)"],
    rows=[
      ["North", "30", "96", "4"],
      ["Central", "35", "92", "8"],
      ["Coast", "25", "90", "10"],
      ["East", "10", "18", "82"],
      ["Country H (all regions)", "100", "85", "15"]],
    description="A table showing, for each of four regions of Country H and for the country as a whole, the region's share of the national population and the percent of people who speak Language A or Language B at home.",
    source="Hypothetical data"),
  stem="A national report on Country H states, \"Only 15 percent of people speak Language B at home, so language is unlikely to divide the country.\" Based on the table, which statement best explains a weakness in this conclusion?",
  options={
    "A": "The regional percentages add up to more than 100, so the national figure is wrong.",
    "B": "Language B is spoken by so few people that it cannot shape any region's identity.",
    "C": "The conclusion should use global-scale data, since languages cross national borders.",
    "D": "Language B is spreading quickly, so it will soon be the national majority language.",
    "E": "The national figure hides that Language B speakers are a large majority in the East region."},
  answer="E",
  explanation="The national number, 15%, is an average for the whole country. Zoom in to the regional scale, and the picture changes: 82% of people in the East speak Language B at home. A group that is small nationally but a large majority in one region can have a strong regional identity, which can become a centrifugal force. Changing the scale of analysis can change the conclusion.",
  whyNot={
    "A": "In each row, Language A and Language B add to 100%, and the regions' population shares add to 100%. The 15% national figure matches the regional data.",
    "B": "In the East, 82% speak Language B at home, so it clearly can shape that region's identity.",
    "C": "The question is about unity inside Country H. Regional data, not global data, show where Language B speakers are concentrated.",
    "D": "The table shows one point in time, so it gives no evidence about how fast Language B is spreading."},
  vocab=["scale of analysis", "centrifugal force", "regionalism"]))

P.append(dict(id="U3-P35", topic="3.2", lo="PSO-3.C", skill="2.B", difficulty="medium",
  stem="Rail systems in several large cities, including Tokyo, Mexico City, and Delhi, set aside some train cars for women only. In Tokyo, rail companies began doing this in response to complaints about the harassment of women on crowded trains. This policy best illustrates how",
  options={
    "A": "time-space convergence has made rush-hour trains much less crowded",
    "B": "religious laws in these cities require men and women to stay apart in public spaces",
    "C": "fewer women now ride public transportation to get to work",
    "D": "concerns about gender and safety can shape how public space is designed and used",
    "E": "cultural relativism leads cities to copy one another's transit systems"},
  answer="D",
  explanation="Your AP course guide says attitudes about gender help shape how people use space. Many women ride crowded trains to work and school. Because of concerns about harassment, some cities reserve cars for women. That changes how a public space is designed and used.",
  whyNot={
    "A": "The policy exists because trains are crowded, not because they have become less crowded.",
    "B": "The stem describes a safety measure on crowded trains, not a religious law. Men and women share most public spaces in these cities.",
    "C": "Women-only cars make sense where many women ride trains, so the policy points to heavy use by women, not less.",
    "E": "Cultural relativism is an attitude toward other cultures. It does not explain this safety policy."},
  vocab=["gender", "use of space", "public space"]))
