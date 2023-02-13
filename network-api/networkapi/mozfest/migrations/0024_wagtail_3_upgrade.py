# Generated by Django 3.2.16 on 2023-02-09 10:15

from django.db import migrations
import networkapi.wagtailpages.pagemodels.blog.blog_topic
import networkapi.wagtailpages.pagemodels.profiles
import wagtail.blocks
import wagtail.blocks.static_block
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('mozfest', '0023_add_accordion_to_mozfest_primary_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mozfestprimarypage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'hr', 'document-link', 'large'], template='wagtailpages/blocks/rich_text_block.html')), ('card_grid', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.blocks.CharBlock(help_text="Alt text for card's image.", required=False)), ('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('body', wagtail.blocks.TextBlock(help_text='Body text of the card.')), ('link_url', wagtail.blocks.CharBlock(help_text='Optional URL that this card should link out to. (Note: If left blank, link will not render.) ', required=False)), ('link_label', wagtail.blocks.CharBlock(help_text='Optional Label for the URL link above. (Note: If left blank, link will not render.) ', required=False))]), help_text='Please use a minimum of 2 cards.'))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('captionURL', wagtail.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False)), ('image_width', wagtail.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('wide', 'Wide'), ('full_width', 'Full Width')], help_text='Wide images are col-12, Full-Width Images reach both ends of the screen (16:6 images recommended for full width)'))])), ('image_text', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'hr', 'document-link'])), ('url', wagtail.blocks.CharBlock(help_text='Optional URL that this image should link out to.', required=False)), ('top_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('image_text_mini', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])), ('image_grid', wagtail.blocks.StructBlock([('grid_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.blocks.CharBlock(help_text='Alt text for this image.', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)), ('square_image', wagtail.blocks.BooleanBlock(default=True, help_text='If left checked, the image will be cropped to be square.', required=False))])))])), ('video', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='For YouTube: go to your YouTube video and click “Share,” then “Embed,” and then copy and paste the provided URL only. For example: https://www.youtube.com/embed/3FIVXBawyQw For Vimeo: follow similar steps to grab the embed URL. For example: https://player.vimeo.com/video/9004979', label='Embed URL')), ('caption', wagtail.blocks.CharBlock(required=False)), ('captionURL', wagtail.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False)), ('video_width', wagtail.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('wide', 'Wide'), ('full_width', 'Full Width')], help_text='Wide videos are col-12, Full-Width videos reach both ends of the screen.'))])), ('iframe', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='Please note that only URLs from allow-listed domains will work.')), ('height', wagtail.blocks.IntegerBlock(help_text='Optional integer pixel value for custom iFrame height', required=False)), ('caption', wagtail.blocks.CharBlock(required=False)), ('captionURL', wagtail.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False)), ('iframe_width', wagtail.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('wide', 'Wide'), ('full_width', 'Full Width')], help_text='Wide iframes are col-12, Full-Width iframes reach both ends of the screen')), ('disable_scroll', wagtail.blocks.BooleanBlock(default=False, help_text='Checking this will add "scrolling=no" to the iframe. Use this if your iframe is rendering an unnecessary scroll bar or whitespace below it.', required=False))])), ('linkbutton', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('URL', wagtail.blocks.CharBlock()), ('styling', wagtail.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')]))])), ('spacer', wagtail.blocks.StructBlock([('size', wagtail.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')]))])), ('single_quote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.RichTextBlock(features=['bold'])), ('attribution', wagtail.blocks.CharBlock(required=False)), ('attribution_info', wagtail.blocks.RichTextBlock(features=['bold', 'link', 'large'], required=False))])), ('pulse_listing', wagtail.blocks.StructBlock([('search_terms', wagtail.blocks.CharBlock(help_text='Test your search at mozillapulse.org/search', label='Search', required=False)), ('max_number_of_results', wagtail.blocks.IntegerBlock(default=6, help_text='Choose 1-12. If you want visitors to see more, link to a search or tag on Pulse.', max_value=12, min_value=0, required=True)), ('only_featured_entries', wagtail.blocks.BooleanBlock(default=False, help_text='Featured items are selected by Pulse moderators.', label='Display only featured entries', required=False)), ('newest_first', wagtail.blocks.ChoiceBlock(choices=[('True', 'Show newer entries first'), ('False', 'Show older entries first')], label='Sort')), ('advanced_filter_header', wagtail.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('issues', wagtail.blocks.ChoiceBlock(choices=[('all', 'All'), ('Decentralization', 'Decentralization'), ('Digital Inclusion', 'Digital Inclusion'), ('Online Privacy & Security', 'Online Privacy & Security'), ('Open Innovation', 'Open Innovation'), ('Web Literacy', 'Web Literacy')])), ('help', wagtail.blocks.ChoiceBlock(choices=[('all', 'All'), ('Attend', 'Attend'), ('Create content', 'Create content'), ('Code', 'Code'), ('Design', 'Design'), ('Fundraise', 'Fundraise'), ('Join community', 'Join community'), ('Localize & translate', 'Localize & translate'), ('Mentor', 'Mentor'), ('Plan & organize', 'Plan & organize'), ('Promote', 'Promote'), ('Take action', 'Take action'), ('Test & feedback', 'Test & feedback'), ('Write documentation', 'Write documentation')], label='Type of help needed')), ('direct_link', wagtail.blocks.BooleanBlock(default=False, help_text='Checked: user goes to project link. Unchecked: user goes to pulse entry', label='Direct link', required=False))])), ('profile_listing', wagtail.blocks.StructBlock([('max_number_of_results', wagtail.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.blocks.CharBlock(default='', required=False))])), ('profile_by_id', wagtail.blocks.StructBlock([('ids', wagtail.blocks.CharBlock(help_text='Show profiles for pulse users with specific profile ids (mozillapulse.org/profile/[##]). For multiple profiles, specify a comma separated list (e.g. 85,105,332).', label='Profile by ID'))])), ('profile_directory', wagtail.blocks.StructBlock([('max_number_of_results', wagtail.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.blocks.CharBlock(default='', required=False)), ('filter_values', wagtail.blocks.CharBlock(default='2019,2018,2017,2016,2015,2014,2013', help_text='Example: 2019,2018,2017,2016,2015,2014,2013', required=True))])), ('recent_blog_entries', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('tag_filter', wagtail.blocks.CharBlock(help_text='Test this filter at foundation.mozilla.org/blog/tags/', label='Filter by Tag', required=False)), ('topic_filter', wagtail.blocks.ChoiceBlock(choices=networkapi.wagtailpages.pagemodels.blog.blog_topic.BlogPageTopic.get_topics, help_text='Test this filter at foundation.mozilla.org/blog/topic/', label='Filter by Topic', required=False)), ('top_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('blog_set', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('top_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False)), ('blog_pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(page_type=['wagtailpages.BlogPage'])))])), ('airtable', wagtail.blocks.StructBlock([('url', wagtail.blocks.URLBlock(help_text="Copied from the Airtable embed code. The word 'embed' will be in the url")), ('height', wagtail.blocks.IntegerBlock(default=533, help_text='The pixel height on desktop view, usually copied from the Airtable embed code'))])), ('typeform', wagtail.blocks.StructBlock([('embed_id', wagtail.blocks.CharBlock(help_text='The embed id of your Typeform page (e.g. if the form is on admin.typeform.com/form/e8zScc6t, the id will be: e8zScc6t)', required=True)), ('button_type', wagtail.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')])), ('button_text', wagtail.blocks.CharBlock(help_text='This is a text prompt for users to open the typeform content', required=True))])), ('datawrapper', wagtail.embeds.blocks.EmbedBlock(help_text='Enter the "visualization only" link of the Datawrapper chart. It looks something like this: https://datawrapper.dwcdn.net/KwSKp/1/', icon='image', template='wagtailpages/blocks/datawrapper_block.html')), ('listing', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.blocks.CharBlock(help_text="Alt text for card's image.", required=False)), ('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('body', wagtail.blocks.RichTextBlock(features=['bold'], help_text='Body text of the card.')), ('link_page', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.', required=False)), ('link_url', wagtail.blocks.CharBlock(help_text='Optional URL that the header should link out to.', required=False))]), help_text='Please use a minimum of 2 cards.', min_num=2))])), ('profiles', wagtail.blocks.StructBlock([('profiles', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('profile', wagtail.snippets.blocks.SnippetChooserBlock(networkapi.wagtailpages.pagemodels.profiles.Profile))]), min_num=1))])), ('article_teaser_block', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('article', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.', page_type=['wagtailpages.ArticlePage'], required=False))]), help_text='Please use a minimum of 3 cards.', min_num=3))])), ('group_listing_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading for the group of cards.', required=False)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.blocks.CharBlock(help_text="Alt text for card's image.", required=False)), ('meta_data', wagtail.blocks.CharBlock(help_text='Optional meta data information for the card.', required=False)), ('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('body', wagtail.blocks.RichTextBlock(features=['bold'], help_text='Body text of the card.')), ('url', wagtail.blocks.CharBlock(help_text='The URL this card should link to.', required=False))])))])), ('image_feature', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).')), ('metadata', wagtail.blocks.CharBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('title_link', wagtail.blocks.PageChooserBlock(help_text='Page that the title should link out to.', required=False)), ('body', wagtail.blocks.CharBlock(required=False))])), ('image_teaser_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('text', wagtail.blocks.RichTextBlock(features=['bold'])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('url_label', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.CharBlock(required=False)), ('styling', wagtail.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')])), ('top_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('text_only_teaser', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('link_page', wagtail.blocks.PageChooserBlock(help_text='Page that the header should link out to.', required=False)), ('link_url', wagtail.blocks.CharBlock(help_text='Optional URL that the header should link out to.', required=False)), ('meta_data', wagtail.blocks.CharBlock(max_length=500)), ('body', wagtail.blocks.TextBlock(help_text='Body text of the card.', max_length=200, required=False))]), help_text='Please use a minimum of 3 cards.', min_num=3))])), ('block_with_aside', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('listing', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt_text', wagtail.blocks.CharBlock(help_text="Alt text for card's image.", required=False)), ('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('body', wagtail.blocks.RichTextBlock(features=['bold'], help_text='Body text of the card.')), ('link_page', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.', required=False)), ('link_url', wagtail.blocks.CharBlock(help_text='Optional URL that the header should link out to.', required=False))]), help_text='Please use a minimum of 2 cards.', min_num=2))])), ('paragraph', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'hr', 'document-link']))], help_text='The wider block that appears on the left on desktop', icon='doc-full', max_num=1)), ('aside', wagtail.blocks.StreamBlock([('aside_content', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading for the card.', required=False)), ('body', wagtail.blocks.TextBlock(help_text='Body text of the card.', required=False))])), ('linkbutton', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('URL', wagtail.blocks.CharBlock()), ('styling', wagtail.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')]))])), ('spacer', wagtail.blocks.StructBlock([('size', wagtail.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')]))]))], help_text='Elements here will appear in the column on the right side of the page on desktop. This can be left blank if you would just like a 2/3 column on the left', icon='doc-full', required=False))])), ('accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading for the Accordion Item')), ('content', wagtail.blocks.StreamBlock([('rich_text', wagtail.blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'link', 'ul', 'ol', 'document-link'])), ('datawrapper', wagtail.embeds.blocks.EmbedBlock(help_text='Enter the "visualization only" link of the Datawrapper chart. It looks something like this: https://datawrapper.dwcdn.net/KwSKp/1/', icon='image', template='wagtailpages/blocks/datawrapper_block.html')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))]))])))])), ('session_slider', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading for the slider.')), ('session_items', wagtail.blocks.StreamBlock([('session_item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('author_subheading', wagtail.blocks.CharBlock(help_text='Author of this session.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image associated with this session.')), ('body', wagtail.blocks.RichTextBlock(help_text='Body text of this card.')), ('video', wagtailmedia.blocks.VideoChooserBlock(help_text='Video that will autoplay when this card is hovered on', required=False)), ('link', wagtail.blocks.StreamBlock([('internal', wagtail.blocks.StructBlock([('link', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.'))])), ('external', wagtail.blocks.StructBlock([('link', wagtail.blocks.URLBlock(help_text='URL that this should link out to.'))]))], help_text='Page or external URL this card will link out to.', max_num=1))]))], help_text='A list of sessions in the slider.')), ('button', wagtail.blocks.StreamBlock([('internal', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Label for this link.')), ('link', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.'))])), ('external', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Label for this link.')), ('link', wagtail.blocks.URLBlock(help_text='URL that this should link out to.'))]))], help_text='Button that appears below the slider.', max_num=1, required=False))])), ('current_events_slider', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading for the slider.')), ('current_events', wagtail.blocks.StreamBlock([('current_event', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Heading of the card.')), ('subheading_link', wagtail.blocks.StreamBlock([('internal', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Label for this link.')), ('link', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.'))])), ('external', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Label for this link.')), ('link', wagtail.blocks.URLBlock(help_text='URL that this should link out to.'))]))], help_text='The link that appears below the card heading.', max_num=1, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image associated with this event.')), ('body', wagtail.blocks.TextBlock(help_text='Body text of the card.')), ('buttons', wagtail.blocks.StreamBlock([('internal', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Label for this link.')), ('link', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.'))])), ('external', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Label for this link.')), ('link', wagtail.blocks.URLBlock(help_text='URL that this should link out to.'))])), ('document', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Label for this link.')), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Document that this should link out to.'))], help_text='An iCal document can be attached here for an "Add to Calendar" button.'))], help_text='A list of buttons that will appear at the bottom of the card.', max_num=2))]))], help_text='A list of current events in the slider.'))])), ('spaces', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('cards', wagtail.blocks.StreamBlock([('space_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(help_text='Heading for the card.')), ('body', wagtail.blocks.TextBlock(help_text='Body text of the card.')), ('link', wagtail.blocks.StreamBlock([('internal', wagtail.blocks.StructBlock([('link', wagtail.blocks.PageChooserBlock(help_text='Page that this should link out to.'))])), ('external', wagtail.blocks.StructBlock([('link', wagtail.blocks.URLBlock(help_text='URL that this should link out to.'))]))], help_text='Page or external URL this card will link out to.', max_num=1))]))], help_text='A list of Spaces Cards.'))])), ('tito_widget', wagtail.blocks.StructBlock([('button_label', wagtail.blocks.CharBlock(help_text='The text to show on the Tito button.')), ('styling', wagtail.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')])), ('event', wagtail.snippets.blocks.SnippetChooserBlock('events.TitoEvent', help_event='The Tito event to be displayed')), ('releases', wagtail.blocks.CharBlock(help_text='Comma-separated list of ticket/release IDs to limit to, e.g. "3elajg6qcxu,6qiiw4socs4"', required=False))])), ('tabbed_profile_directory', wagtail.blocks.StructBlock([('tabs', wagtail.snippets.blocks.SnippetChooserBlock('wagtailpages.PulseFilter', help_text=('Tabs are created based on the selected pulse filter ', 'and the first option in the snippet will be the first tab showing open on the page.'))), ('subfilters', wagtail.blocks.StreamBlock([('filter', wagtail.snippets.blocks.SnippetChooserBlock('wagtailpages.PulseFilter'))], max_num=1, required=False)), ('advanced_filter_header', wagtail.blocks.static_block.StaticBlock(admin_text='Note that the filter not be used if selected as the tabs filter or as one of the subfilters. For example, if the tabs filter profile types, the profile type field below will be ignored.', label='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------')), ('profile_type', wagtail.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.blocks.CharBlock(default='', required=False))])), ('newsletter_signup', wagtail.blocks.StructBlock([('signup', wagtail.snippets.blocks.SnippetChooserBlock('wagtailpages.Signup'))]))], use_json_field=True),
        ),
    ]
