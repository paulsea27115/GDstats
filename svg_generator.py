def generate_svg(owner, godot_logo_url, total_commit):
    svg = f"""
    <svg
        width="700"
        height="150"
        viewBox="0 0 700 150"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
    >
      <style>
        * {{
          font-family: 'Inter', 'Noto Sans KR', sans-serif;
        }}

        text {{
          fill: black;
        }}

        .profile-image {{
          filter: drop-shadow(rgba(0, 212, 151, 0.6) 0px 4px 8px);
        }}

        .header {{
          font-weight: 800;
          font-size: 20px;
        }}

        .bio {{
          font-size: 16px;
          overflow: hidden;
          text-overflow: ellipsis;
          display: inline-block;
          width: 400px;
          height: 30px;
          white-space: nowrap;
        }}

        .rank {{
          color: rgb(39, 226, 164);
          font-weight: 700;
          font-size: 24px;
        }}

        .exp-progress {{
          color: rgb(138, 143, 149);
          font-weight: 400;
          font-size: 14px;
        }}

        .flex-row {{
          display: flex;
          flex-direction: row;
          width: 235px;
          height: 50px;
          justify-content: flex-end;
        }}

        .item-box {{
          margin-left: 12px;
          padding-right: 10px;
          border-right: 1px solid black;
        }}

        .item-title {{
          font-weight: 400;
          font-size: 16px;
        }}

        .item-number {{
          font-weight: 600;
          font-size: 22px;
          text-align: right;
        }}
      </style>
      <rect
        data-testid="card-bg"
        x="0.5"
        y="0.5"
        rx="4.5"
        height="99%"
        stroke="#E4E2E2"
        width="699"
        fill="#FFFEFE"
      />
      <g class="profile" data-testid="card-title" transform="translate(20, 20)">
        <foreignObject class="profile-image" width="300" height="300" x="-20" y="-45">
          <xhtml:img width="120" height="120" src="{godot_logo_url}"/>
        </foreignObject>
        <text x="105" y="20.5" class="header">{owner}</text>
        <g transform="translate(105, 28)">
          <foreignObject width="400" height="100">
            <xhtml:span class="bio">test</xhtml:span>
          </foreignObject>
        </g>
      </g>

      <g transform="translate(125, 80)">
        <foreignObject width="300" height="300">
          <xhtml:div class="rank">Noob</xhtml:div>
          <xhtml:div class="exp-progress">10/100</xhtml:div>
        </foreignObject>

        <foreignObject width="300" height="300" x="305" y="3">
          <xhtml:div class="flex-row box">
            <xhtml:div class="item-box box">
              <xhtml:div class="item-title">Total Commits</xhtml:div>
              <xhtml:div class="item-number">{total_commit}</xhtml:div>
            </xhtml:div>
          </xhtml:div>
        </foreignObject>
      </g>

      <g class="badge" data-testid="card-badge" transform="translate(585, 10)">
      </g>
    </svg>
    """
    return svg
