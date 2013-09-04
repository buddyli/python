<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>Member List</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>Passport</th>
                    <th>Username</th>
                    <th>Country</th>
                    <th>Mobile</th>
                    <th>Shares</th>
                    <th>Action</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'members' in data:
                    %for member in data['members']:
                    <tr class="${loop.cycle('alt', 'odd')}">
                        <td>${ member['passport'] if 'passport' in member else '--' }</td>
                        <td>${ member['username'] if 'username' in member else '--' }</td>
                        <td>${ member['country'] if 'country' in member else '--' }</td>
                        <td>${ member['mobile'] if 'mobile' in member else '--' }</td>
                        <td>${ member['shares'] if 'shares' in member else '--' }</td>
                        <td><a class="edit" href="/manage/member/edit?_id=${ member['_id'] }">edit</a><a class="delete" href="/manage/member/delete?_id=${ member['_id'] }${ '&_uniq=%s' % data['_uniq'] if '_uniq' in data else ''}" onclick="javascript:return confirm('Yes or No?')">delete</a></td>
                    </tr>
                    %endfor
                %endif
            </tbody>
        </table><!-- END Table -->
        <div class="box">
            <!-- Page Navigation -->
            %if 'pagenation' in data:
            <ul class="paginator">
                %for p in data['pagenation']:
                <li class="${ 'current' if p == data['cur_page'] else ''}"><a href="/manage/member/list?page=${ p }${ '&_uniq=%s' % data['_uniq'] if '_uniq' in data else ''}">${ p }</a></li>
                %endfor
            </ul>
            %endif
        <!-- /Page Navigation -->
        </div>
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>